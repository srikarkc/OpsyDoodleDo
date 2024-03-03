terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.5"
    }
  }
}

provider "google" {
  project = "red-grid-387319"
  region  = "us-west1"
  zone    = "us-west1-b"
}

resource "google_compute_instance" "my_instance" {
  name         = "vehicle-dynamics-calculator"
  machine_type = "e2-medium"
  zone         = "us-west1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20231213"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }
}
