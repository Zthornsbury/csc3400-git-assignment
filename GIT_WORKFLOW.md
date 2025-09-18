# Git Workflow Documentation

   ## Branching Strategy
   - **main branch**: Production-ready code only
   - **feature branches**: New features (feature/feature-name)
   - **hotfix branches**: Critical fixes (hotfix/fix-name)
   - **release branches**: Release preparation (release/version-number)

   ## Commit Message Conventions
   - Use present tense ("Add feature" not "Added feature")
   - Keep first line under 50 characters
   - Use descriptive messages
   - Examples:
     - "Add user authentication system"
     - "Fix division by zero error"
     - "Update README with installation instructions"

   ## Code Review Process
   1. Create feature branch from main
   2. Develop feature with regular commits
   3. Push branch to remote repository
   4. Create pull request with detailed description
   5. Request review from team members
   6. Address review comments
   7. Merge after approval

   ## Release Workflow
   1. Create release branch from main
   2. Update version numbers and documentation
   3. Test thoroughly
   4. Merge to main and tag with version
   5. Deploy to production
   6. Merge back to development branches

   ## Common Git Commands Reference

   ### Repository Setup
   - `git init` - Initialize new repository
   - `git clone <url>` - Clone existing repository
   - `git remote add origin <url>` - Add remote repository

   ### Basic Operations
   - `git status` - Check repository status
   - `git add <file>` - Stage files for commit
   - `git commit -m "message"` - Commit staged changes
   - `git push` - Push commits to remote
   - `git pull` - Pull changes from remote

   ### Branching
   - `git branch` - List branches
   - `git checkout -b <branch>` - Create and switch to new branch
   - `git checkout <branch>` - Switch to existing branch
   - `git merge <branch>` - Merge branch into current branch
   - `git branch -d <branch>` - Delete branch

   ### Information
   - `git log` - View commit history
   - `git log --oneline` - Compact commit history
   - `git log --graph` - Visual branch history
   - `git diff` - Show changes between commits

   ### Conflict Resolution
   - `git status` - Identify conflicted files
   - Edit files to resolve conflicts
   - `git add <resolved-file>` - Mark conflicts as resolved
   - `git commit` - Complete merge