#!/usr/bin/env bash
# GORILLA UNLEASHED - Branding & UI Port (Debian -> Windows) - v2
# This script ports the "Total Purge" UI logic and massive Gorilla logos.

SOURCE_ROOT="/home/gorilla/firefox_build/firefox"
ICONS_DIR="/home/gorilla/Documents/master_build_windows/icons"
WINDOWS_OVERLAY="/home/gorilla/Documents/master_build_windows/icons/Windows"
LINUX_OVERLAY="/home/gorilla/Documents/master_build_windows/source_overlay"

echo "=== 1. CONVERTING ICONS FOR WINDOWS ==="
# Replace the default firefox.ico with our custom one
cp "$ICONS_DIR/firefox.ico" "$SOURCE_ROOT/browser/branding/official/firefox.ico"
cp "$ICONS_DIR/firefox.ico" "$SOURCE_ROOT/browser/branding/aurora/firefox.ico"

# Replace standard PNG sizes (whitelisting Ivy Bridge icons)
for size in 16 32 48 64 128 256; do
    if [ -f "$ICONS_DIR/default$size.png" ]; then
        cp "$ICONS_DIR/default$size.png" "$SOURCE_ROOT/browser/branding/official/default$size.png"
        cp "$ICONS_DIR/default$size.png" "$SOURCE_ROOT/browser/branding/aurora/default$size.png"
    fi
done

echo "=== 2. APPLYING 'TOTAL PURGE' NEW TAB UI ==="
# Porting the massive 750px logo and centered layout
mkdir -p "$SOURCE_ROOT/browser/extensions/newtab/css/"
cp "$LINUX_OVERLAY/browser/extensions/newtab/css/activity-stream.css" "$SOURCE_ROOT/browser/extensions/newtab/css/activity-stream.css"
cp "$LINUX_OVERLAY/browser/locales/en-US/browser/newtab/newtab.ftl" "$SOURCE_ROOT/browser/locales/en-US/browser/newtab/newtab.ftl"

echo "=== 3. APPLYING ABOUT DIALOG TWEAKS ==="
# Porting the 500px logo and purple background logic
cp "$LINUX_OVERLAY/browser/base/content/aboutDialog.css" "$SOURCE_ROOT/browser/base/content/aboutDialog.css"
cp "$LINUX_OVERLAY/browser/base/content/aboutDialog.xhtml" "$SOURCE_ROOT/browser/base/content/aboutDialog.xhtml"
cp "$LINUX_OVERLAY/browser/locales/en-US/browser/aboutDialog.ftl" "$SOURCE_ROOT/browser/locales/en-US/browser/aboutDialog.ftl"

# Ensure the logo is available in the branding content
cp "$ICONS_DIR/about-logo.png" "$SOURCE_ROOT/browser/branding/official/content/about-logo.png"
cp "$ICONS_DIR/about-logo@2x.png" "$SOURCE_ROOT/browser/branding/official/content/about-logo@2x.png"

echo "=== 4. INJECTING WINDOWS-OPTIMIZED USER.JS ==="
# The user.js goes into the default browser profile template
cp "$WINDOWS_OVERLAY/user.js" "$SOURCE_ROOT/browser/app/profile/firefox.js"

echo "=== 5. UPDATING BRANDING TEXT & FLAVOR ==="
# Update the Brand name in locales
find "$SOURCE_ROOT/browser/locales/en-US/" -type f -name "*.ftl" -exec sed -i 's/Firefox/Gorilla Unleashed/g' {} +

# Flavor adjustment for Windows users
sed -i 's/Apple Moron/Windows Moron/g' "$SOURCE_ROOT/browser/locales/en-US/browser/newtab/newtab.ftl"

echo "=== BRANDING APPLIED: GORILLA UNLEASHED WINDOWS EDITION ==="
