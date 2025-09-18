# Conflict Resolution Documentation

   ## Conflict 1: README Title Conflict
   **Date:** "9/17/2025"
   **Files:** README.md
   **Branches:** main (both repositories)

   ### Conflict Description:
   Both repositories modified the project title simultaneously, creating a merge conflict.

   ### Resolution Process:
   1. Pulled latest changes using `git pull origin main`
   2. Git automatically marked conflict areas with markers
   3. Manually edited README.md to combine both titles meaningfully
   4. Added descriptive subtitle to incorporate both concepts
   5. Removed conflict markers (<<<<<<, ======, >>>>>>)
   6. Committed resolved changes

   ### Final Resolution:
   Combined titles into "Advanced CSC 3400 Calculator Application" with subtitle explaining the project scope.

   ## Conflict 2: Calculator Module Header Conflict
   **Date:** "9/17/2025"
   **Files:** calculator.py
   **Branches:** main (both repositories)

   ### Conflict Description:
   Different header comments were added to the calculator module from both repositories.

   ### Resolution Process:
   1. Identified conflict in calculator.py header
   2. Used merge strategy to combine both descriptive elements
   3. Created unified header that included version and description
   4. Tested code functionality after resolution

   ### Final Resolution:
   Combined headers into "Advanced Mathematical Calculator - Version 1.0"

   ## Tools Used:
   - Command line Git
   - Text editor for manual conflict resolution
   - Git status and log commands for tracking

   ## Best Practices Applied:
   - Always pull before pushing
   - Carefully review conflict markers
   - Test functionality after resolution
   - Commit with clear resolution messages