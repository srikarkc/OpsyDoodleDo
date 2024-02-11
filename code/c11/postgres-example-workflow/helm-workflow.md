To deploy the PostgreSQL setup to a Kubernetes cluster in a production environment using Helm, you'll follow a structured approach. Helm simplifies Kubernetes application deployment by packaging applications into charts. For this example, I'll outline the steps to create a Helm chart for PostgreSQL and provide basic templates for the necessary components like `StatefulSet` and `Service`, following Helm's best practices.

### Step 1: Create the Helm Chart

1. **Initialize the Chart**:
   Create a new directory for your chart and initialize it.

   ```shell
   helm create postgres-chart
   ```

   This command creates a new chart directory with a sample chart.

2. **Remove Unnecessary Files**:
   Navigate to the `postgres-chart` directory and clean up unnecessary files.

   ```shell
   cd postgres-chart
   rm -rf templates/* values.yaml
   ```

### Step 2: Define the Chart Configuration

1. **Create `values.yaml`**:
   Create a new `values.yaml` in the `postgres-chart` directory. This file will hold all configurable options for your chart.

   ```yaml
   # values.yaml
   postgres:
     image: my-postgres-image:latest
     dbName: mydatabase
     user: myuser
     password: mypassword
     storage:
       size: 1Gi
   ```

2. **Add Production-Ready Features**:
   - **Security**: Ensure your image and deployment configurations adhere to security best practices, like using non-root containers.
   - **High Availability**: Consider replication and automated failover. You might need to use a more advanced setup or an operator like CrunchyData Postgres Operator for production-grade deployments.

### Step 3: Add Templates

1. **StatefulSet Template**:
   Create a `statefulset.yaml` file in the `templates` directory. This file defines the StatefulSet for PostgreSQL using values from `values.yaml`.

   ```yaml
   # templates/statefulset.yaml
   apiVersion: apps/v1
   kind: StatefulSet
   metadata:
     name: {{ include "postgres-chart.fullname" . }}
   spec:
     serviceName: "postgres"
     replicas: 1
     selector:
       matchLabels:
         app: {{ include "postgres-chart.name" . }}
     template:
       metadata:
         labels:
           app: {{ include "postgres-chart.name" . }}
       spec:
         securityContext:
           fsGroup: 999
         containers:
         - name: postgres
           image: {{ .Values.postgres.image }}
           ports:
           - containerPort: 5432
           env:
           - name: POSTGRES_DB
             value: {{ .Values.postgres.dbName }}
           - name: POSTGRES_USER
             value: {{ .Values.postgres.user }}
           - name: POSTGRES_PASSWORD
             valueFrom:
               secretKeyRef:
                 name: {{ include "postgres-chart.fullname" . }}-secret
                 key: postgres-password
           volumeMounts:
           - name: postgres-storage
             mountPath: /var/lib/postgresql/data
     volumeClaimTemplates:
     - metadata:
         name: postgres-storage
       spec:
         accessModes: ["ReadWriteOnce"]
         resources:
           requests:
             storage: {{ .Values.postgres.storage.size }}
   ```

2. **Service Template**:
   Create a `service.yaml` file in the `templates` directory for the LoadBalancer service.

   ```yaml
   # templates/service.yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: {{ include "postgres-chart.fullname" . }}-service
   spec:
     type: LoadBalancer
     ports:
     - port: 5432
       targetPort: 5432
       protocol: TCP
     selector:
       app: {{ include "postgres-chart.name" . }}
   ```

3. **Secrets for Sensitive Data**:
   For production environments, sensitive data like passwords should not be stored in `values.yaml`. Instead, use Kubernetes secrets and reference them in your templates.

   Create a `templates/secrets.yaml`:

   ```yaml
   # templates/secrets.yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: {{ include "postgres-chart.fullname" . }}-secret
   type: Opaque
   data:
     postgres-password: {{ .Values.postgres.password | b64enc | quote }}
   ```

### Step 4: Deploying the Chart

1. **Package Your Chart**:
   Run `helm package postgres-chart` to create a chart package.

2. **Deploy the Chart**:
   Use `helm install` to deploy your chart to the Kubernetes cluster.

   ```shell
   helm install postgres-release ./postgres-chart
   ```

3. **Update Secrets**:
   Before deploying, make sure to create the secret or use an existing secret for the