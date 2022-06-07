
resource "github_repository" "devOpsLab" {
  name        = "devOpsLab"
  description = "Solutions to DevOps labs"

  visibility = "public"

  default_branch = "master"
}

data "github_user" "behouba" {
  username = "behouba"
}



resource "github_branch_protection" "master_branch_protection" {
  repository_id = github_repository.devOpsLab.node_id


  pattern          = "master"
  enforce_admins   = true
  allows_deletions = false


  required_pull_request_reviews {
    dismiss_stale_reviews = true
    restrict_dismissals   = true
    dismissal_restrictions = [
      data.github_user.behouba.node_id,
      #   github_team.devOpsLab.node_id,
    ]
  }

}