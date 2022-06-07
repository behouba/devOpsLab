terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }

  cloud {
    organization = "behouba"
    workspaces {
      name = "devOpsLab"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
   token="${GITHUB_TOKEN}"
}

