# Create a new repository
resource "github_repository" "repo" {
  name               = "Terraform-Initialized-Repo"
  description        = "Test repository created by Terraform for IU S24 DevOps course."
  visibility         = "public"
  has_issues         = false
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}

# Set default branch to 'main'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

# Branch protection
resource "github_branch_protection" "repo-default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

# Import S24-devops-labs repository
resource "github_repository" "S24-devops-labs" {
    name = "S24-devops-labs"
}

# Branch protection
resource "github_branch_protection" "devops-default" {
  repository_id                   = github_repository.S24-devops-labs.id
  pattern                         = "main"
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}