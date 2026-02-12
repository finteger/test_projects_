from playwright.sync_api import Page, expect
import time
import http.server
import socketserver
import threading
import os 

#global server instance
server = None
server_thread = None

def start_server(port=8000):
    #start a HTTP server in a background thread
    global server, server_thread
    
    #create server
    handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer(("", port), handler)
    
    #run the server daemon thread (will exit when main thread exits)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    
    print(f'Server is connected at http://localhost:{port}')
    
    time.sleep(1)  #give the server a moment to start

#stop the server
def stop_server():
    global server
    if server:
        server.shutdown()
        print('Server is shutdown')
        

def test_add_todo_item(page: Page):
    print('\n=== Running test: Add To-Do Item ===')
    
    #navigate to the app
    page.goto('http://localhost:8000/todo_list.html')
    
    print('Adding a new task...')
    #find the input element and fill it in with a new task
    page.get_by_test_id('todo-input').fill('Buy groceries')
    
    #click the submit button 
    page.get_by_role("button", name="Submit").click()
    
    page.wait_for_timeout(500)
    
    #verify that the task appears on the UL list
    todo_items = page.get_by_test_id('todo-item')
    assert todo_items.count() == 1, "Should have 1 to-do item after adding"
    
    #verify the counter updates
    total_count = page.locator('#total-count').text_content()
    assert total_count == 1, f'Total count should be 1 after adding, but got {total_count}' 
    
    print("Task added succesfully!")
    
    page.wait_for_timeout(500)
    
        
        
#run our suite of tests 
def run_all_tests():
    try:
        test_add_todo_item()    
        #to-do implement tests
    except AssertionError as e:
        print(f'Test failed: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')    
        
 
#runs the document as the main script     
if __name__ == "__main__":
    start_server(port=8000)
    try:
        run_all_tests()
    finally:
        stop_server()