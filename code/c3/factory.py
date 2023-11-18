# Factory Machine Maintenance

# List of Tuples
machines = [(101, "Oil Change"), (102, "Filter Replacement"), (103, "Belt Inspection")]

# Set
completed_maintenance = set()

for machine in machines:
    # Unpacking Tuple
    machine_id, task = machine
    print(f"Performing {task} on {machine_id}.")
    completed_maintenance.add(machine_id)

#print("Completed set of maintenance: " + completed_maintenance)

# while loop
parts_used = ["Oil", "Filter", "Belt", "Oil", "Belt"]
parts_inventory = {}

while parts_used:
    part = parts_used.pop()
    if part in parts_inventory:
        parts_inventory[part] += 1
    else:
        parts_inventory[part] = 1

print(parts_inventory)