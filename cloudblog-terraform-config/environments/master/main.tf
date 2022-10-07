terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}


provider "google" {

  project = var.project_id
  region  = "us-central1"
  zone    = "us-central1-c"

}


resource "google_app_engine_application" "gaeblog" {
  project     = var.project_id
  location_id = "us-west4"
}

resource "google_app_engine_firewall_rule" "firewall_rule" {
  source_range = var.source_range
  action       = var.action
  description  = var.description
  priority     = var.priority
}

resource "google_project_service" "sqladmin" {
  project            = var.project_id
  service            = var.apis[0]
  disable_on_destroy = false
}

resource "google_project_service" "secretmanager" {
  project            = var.project_id
  service            = var.apis[1]
  disable_on_destroy = false
}

resource "google_project_service" "cloudbuild" {
  project            = var.project_id
  service            = var.apis[2]
  disable_on_destroy = false
}

resource "google_project_service" "cloudstorage" {
  project            = var.project_id
  service            = var.apis[3]
  disable_on_destroy = false
}

resource "google_project_service" "bigquery" {
  project            = var.project_id
  service            = "bigquery.googleapis.com"
  disable_on_destroy = false
}



