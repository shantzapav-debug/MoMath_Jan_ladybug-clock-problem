# Quick launcher for the Streamlit dashboard
# This script runs the dashboard and provides connection information

import subprocess
import sys
import os

# Set environment variable to skip email prompt
os.environ['STREAMLIT_CLIENT_TOOLBARHIDDEN'] = 'true'
os.environ['STREAMLIT_LOGGER_LEVEL'] = 'error'

print("=" * 70)
print("🐞 LADYBUG CLOCK PROBLEM - STREAMLIT DASHBOARD")
print("=" * 70)
print()
print("🚀 Starting Streamlit app...")
print()
print("📱 Open your browser and go to: http://localhost:8501")
print()
print("📊 Features available:")
print("   • 📊 Live Simulation - Watch the ladybug move in real-time")
print("   • 🎬 Batch Simulations - Run multiple simulations")
print("   • 📈 Statistics - Full analysis with 50,000 simulations")
print("   • 📚 How It Works - Learn the theory")
print()
print("=" * 70)
print()

# Run streamlit
subprocess.run([
    sys.executable, '-m', 'streamlit', 'run', 
    'streamlit_dashboard.py',
    '--logger.level=error'
])
