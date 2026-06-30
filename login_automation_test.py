from playwright.sync_api import sync_playwright

def test_secure_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Navigate to a safe, real practice login webpage
        print("STEP: Navigating to practice login page...")
        page.goto("https://herokuapp.com")
        
        # 2. Simulate a user typing into the Username field
        print("STEP: Typing username...")
        page.fill("input#username", "tomsmith") # 'tomsmith' is the correct test username
        
        # 3. Simulate a user typing into the Password field
        print("STEP: Typing password...")
        page.fill("input#password", "SuperSecretPassword!") # The correct test password
        
        # 4. Simulate a user clicking the 'Login' button
        print("STEP: Clicking the login button...")
        page.click("button[type='submit']")
        
        # 5. QA Verification: Check if we successfully logged in by looking for a success message
        print("STEP: Verifying login success...")
        success_message = page.locator("div#flash").text_content()
        
        if "You logged into a secure area!" in success_message:
            print("TEST PASSED: Login automation works perfectly!")
        else:
            print("TEST FAILED: Could not log in!")
            
        browser.close()

# Run the test
test_secure_login()
