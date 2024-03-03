resource "google_compute_instance" "vm_instance_a" {
  name         = var.instance_name
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "debian-10-buster-v20240213"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }
}