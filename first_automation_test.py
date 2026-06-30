from playwright.sync_api import sync_playwright

def test_guc_website():
    # 1. Start the automation engine
    with sync_playwright() as p:
        
        # 2. Launch a real visible browser (headless=False means we want to see it)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 3. Navigate to a real website (let's use your university as a test target!)
        print("STEP: Navigating to GUC website...")
        page.goto("https://guc.edu.eg")
        
        # 4. QA Verification: Check if the page title is correct
        title = page.title()
        print(f"VERIFICATION: The page title is: {title}")
        
        # 5. Safety check to make sure we actually landed on the right site
        if "German University in Cairo" in title:
            print("TEST PASSED: Successfully loaded the correct university homepage!")
        else:
            print("TEST FAILED: Title does not match!")
            
        # 6. Clean up and close the browser session
        browser.close()

# Execute the test function directly
test_guc_website()

