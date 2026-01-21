#!/usr/bin/env python
"""Test script to verify clock positioning is correct"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Draw clock circle
circle = Circle((0, 0), 1.2, fill=False, edgecolor='black', linewidth=3)
ax.add_patch(circle)

# Draw hour positions with CORRECTED formula
num_positions = 12
for i in range(1, num_positions + 1):
    # CORRECTED: removed (i-1), now just use i
    angle = np.pi/2 - i * 2 * np.pi / num_positions
    x = 1.0 * np.cos(angle)
    y = 1.0 * np.sin(angle)
    
    # Draw position circle
    ax.scatter(x, y, s=300, c='#ffcccc', marker='o', edgecolors='black', linewidth=2, zorder=5)
    
    # Draw number
    text_x = 1.35 * np.cos(angle)
    text_y = 1.35 * np.sin(angle)
    ax.text(text_x, text_y, str(i), ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Print position for verification
    print(f"Position {i:2d}: angle={angle:.4f} rad ({np.degrees(angle):.1f}°), coords=({x:.3f}, {y:.3f})")

# Highlight key positions
key_positions = {
    12: "TOP",
    3: "RIGHT",
    6: "BOTTOM",
    9: "LEFT"
}

print("\n✅ KEY POSITIONS:")
for pos, label in key_positions.items():
    angle = np.pi/2 - pos * 2 * np.pi / 12
    x = np.cos(angle)
    y = np.sin(angle)
    print(f"Position {pos:2d} ({label:6s}): ({x:6.3f}, {y:6.3f})")

# Add center circle for aesthetics
center_circle = Circle((0, 0), 0.15, fill=True, facecolor='black', edgecolor='black', linewidth=2)
ax.add_patch(center_circle)

ax.set_title("CORRECTED Clock Face - Positions in Correct Order", fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('clock_test.png', dpi=150, bbox_inches='tight')
print("\n✅ Test visualization saved as 'clock_test.png'")
print("\n✅ VERIFICATION:")
print("   12 should be at TOP (y ≈ 1.0, x ≈ 0.0)")
print("   3 should be at RIGHT (x ≈ 1.0, y ≈ 0.0)")
print("   6 should be at BOTTOM (y ≈ -1.0, x ≈ 0.0)")
print("   9 should be at LEFT (x ≈ -1.0, y ≈ 0.0)")
