# Specify the provider (GCP, AWS, Azure)
provider "google" {
credentials = "${file("credentials-demo.json")}"
project = "alien-works-193006"
region = "us-central1"
}