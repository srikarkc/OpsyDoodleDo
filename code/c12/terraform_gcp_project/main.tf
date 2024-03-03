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
  zone = "us-west1-b"
}


