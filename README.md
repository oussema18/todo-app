# Todo App — CI/CD Practice

A minimal Python to-do list app, built specifically to practice setting up a
CI pipeline with GitHub Actions.

## What's here
- `todo.py` — the app itself (add, complete, remove, list tasks)
- `test_todo.py` — automated tests (pytest)
- `.github/workflows/ci.yml` — the CI pipeline definition
- `requirements.txt` — dependencies

## Run it locally
```bash
pip install -r requirements.txt
pytest -v        # run tests
python todo.py   # run the app
```

## Push to GitHub to see CI in action
1. Create a new empty repo on github.com (no README/gitignore, keep it empty)
2. From this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: todo app with CI pipeline"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. Go to the "Actions" tab on your GitHub repo — you'll see the CI pipeline
   run automatically, install dependencies, run all 5 tests, and run the app.

## Try breaking it on purpose
Edit `test_todo.py` and change an assertion to something wrong (e.g.
`assert todos.list_open() == ["wrong"]`), commit, and push. Watch the
Actions tab turn red — that's CI catching a broken change before it
reaches anyone else.
