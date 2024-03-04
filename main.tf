terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.17.0"
    }
  }
}

provider "google" {
  credentials = "./keys/mycred.json"
  project     = "terraform-demo-415218"
  region      = "europe-west3"
}