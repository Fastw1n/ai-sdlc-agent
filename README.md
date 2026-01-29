1. User creates Issue in app
2. GitHub Action triggers Code Agent
3. Code Agent:
   - reads Issue
   - modifies code
   - creates PR
4. CI runs
5. Reviewer Agent:
   - analyzes diff + CI
   - comments in PR
6. If fail → repeat (max 3 times)
