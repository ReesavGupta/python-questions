from collections import deque

class BrowserHistory():
    def __init__(self, max_size = 5):
        self.history = deque()
        self.forward_stack = deque()
        self.max_len = max_size

    def add_new_page(self, page :str):
        if len(self.history)  == self.max_len:
            self.history.popleft()
        self.history.append(page)
        self.forward_stack.clear()
        self._print_state(f"added new page: {page}")

    def go_back(self):
        if len(self.history) > 1:
            last_page = self.history.pop()
            self.forward_stack.append(last_page)
            self._print_state(f"Back to: {self.history[-1]}")
        else:
            self._print_state("Cannot go back further.")
    def go_forward(self):
        if self.forward_stack:
            forward_page = self.forward_stack.pop()
            if len(self.history) == self.max_len:
                self.history.popleft()
            self.history.append(forward_page)
            self._print_state(f"Forward to: {forward_page}")
        else:
            self._print_state("No forward history.")


    def _print_state(self, action):
        print(f"\nAction: {action}")
        print(f"History: {list(self.history)}")
        print(f"Forward Stack: {list(self.forward_stack)}")


if __name__ == "__main__":
    browser = BrowserHistory()

    browser.add_new_page("google.com")
    browser.add_new_page("wikipedia.org")
    browser.add_new_page("openai.com")
    browser.add_new_page("github.com")
    browser.add_new_page("stackoverflow.com")
    browser.add_new_page("reddit.com")  

    browser.go_back()
    browser.go_back()

    browser.go_forward()

    browser.add_new_page("news.ycombinator.com")  