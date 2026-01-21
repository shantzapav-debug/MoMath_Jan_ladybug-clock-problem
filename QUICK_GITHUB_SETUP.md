# 🚀 Quick Start - Deploy to GitHub in 5 Minutes

## Option 1: Automated Setup (Recommended)

1. **Run the setup script:**
   ```bash
   setup_github.bat
   ```

2. **Follow the prompts:**
   - Enter your GitHub username
   - Enter your email
   - Enter repository name
   - Create repository on GitHub (script will guide you)
   - Paste the clone URL
   - Script handles everything else!

---

## Option 2: Manual Setup (Step-by-Step)

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Name it: `ladybug-clock-problem`
3. Select **Public**
4. Check "Add a README file"
5. Choose Python for `.gitignore`
6. Choose MIT License
7. Click **Create repository**

### Step 2: Copy Repository URL
- Click the green **Code** button
- Copy the **HTTPS URL** (looks like: `https://github.com/YOUR-USERNAME/ladybug-clock-problem.git`)

### Step 3: Set Up Local Repository
```powershell
# Navigate to project folder
cd "c:\Users\2025\Documents\MoMath"

# Initialize git
git init

# Configure your identity
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Add GitHub as remote
git remote add origin https://github.com/YOUR-USERNAME/ladybug-clock-problem.git

# Verify connection
git remote -v
```

### Step 4: Create Key Files
**Create `.gitignore`:**
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
venv/
ENV/
.vscode/
.idea/
*.swp
.DS_Store
corrected_clock.png
clock_test.png
```

**Create `requirements.txt`:**
```
streamlit==1.28.0
matplotlib==3.8.2
seaborn==0.13.0
pandas==2.1.3
numpy==1.24.3
```

### Step 5: Push to GitHub
```powershell
# Stage all files
git add .

# First commit
git commit -m "Initial commit: Ladybug Clock Problem Streamlit dashboard"

# Fix branch name if needed (default: main)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 6: Verify on GitHub
- Visit your repository: `https://github.com/YOUR-USERNAME/ladybug-clock-problem`
- All files should be visible!

---

## 🌐 Deploy to Streamlit Cloud (Optional)

1. Go to https://streamlit.io/cloud
2. Click **Sign in with GitHub**
3. Click **New app**
4. Select:
   - **Repository:** `YOUR-USERNAME/ladybug-clock-problem`
   - **Branch:** `main`
   - **Main file path:** `streamlit_dashboard.py`
5. Click **Deploy**

**Your app will be live at:** `https://share.streamlit.io/YOUR-USERNAME/ladybug-clock-problem`

---

## ✅ Quick Checklist

- [ ] GitHub account created
- [ ] Git installed on computer
- [ ] Repository created on GitHub
- [ ] Local git initialized
- [ ] Files committed
- [ ] Pushed to GitHub
- [ ] Repository visible on GitHub website
- [ ] (Optional) Deployed to Streamlit Cloud

---

## 🔧 Troubleshooting

**Push fails with authentication error:**
```powershell
# Use Personal Access Token instead
# 1. Go to GitHub → Settings → Developer settings → Personal access tokens
# 2. Create new token with 'repo' scope
# 3. Use this format: https://USERNAME:TOKEN@github.com/USERNAME/REPO.git
git remote set-url origin https://USERNAME:TOKEN@github.com/YOUR-USERNAME/ladybug-clock-problem.git
git push -u origin main
```

**Branch name is 'master' instead of 'main':**
```powershell
git branch -M main
git push -u origin main
```

**Need to change what's already pushed:**
```powershell
# Fix last commit message
git commit --amend -m "New message"
git push --force-with-lease

# Undo last commit
git reset --soft HEAD~1
git commit -m "Fixed commit"
git push --force-with-lease
```

---

## 📊 Project Structure on GitHub

```
ladybug-clock-problem/
├── streamlit_dashboard.py     # Main app
├── Jan_moMath.py              # Core simulation
├── run_dashboard.py           # Launcher
├── test_clock.py              # Verification
├── requirements.txt           # Dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project description
├── LICENSE                    # MIT License
├── GITHUB_HOSTING_GUIDE.md    # Detailed guide
├── YOUTUBE_SCRIPTS.md         # Video scripts
├── PROJECT_OVERVIEW.md        # Technical overview
└── [other documentation]
```

---

## 📱 Share Your Project

### Direct Link
Share the GitHub URL: `https://github.com/YOUR-USERNAME/ladybug-clock-problem`

### GitHub Badge
Add to your README:
```markdown
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github&logoColor=white)](https://github.com/YOUR-USERNAME/ladybug-clock-problem)
```

### Streamlit Badge
If deployed to Streamlit Cloud:
```markdown
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/YOUR-USERNAME/ladybug-clock-problem)
```

---

**Questions?** Check `GITHUB_HOSTING_GUIDE.md` for detailed explanations!
