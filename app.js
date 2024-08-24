document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.querySelector('.chat-body');
    const userInput = document.getElementById('user-input');
    const sendButton = document.querySelector('.send-btn');

    // Function to add user message to chat
    function addUserMessage(message) {
        const userMessage = document.createElement('div');
        userMessage.classList.add('user-message');
        userMessage.textContent = message;
        chatBody.appendChild(userMessage);
        chatBody.scrollTop = chatBody.scrollHeight; // Scroll to the bottom
    }

    // Function to handle the send button click
    sendButton.addEventListener('click', () => {
        const message = userInput.value.trim();
        if (message) {
            addUserMessage(message);
            userInput.value = ''; // Clear input field
            resizeInput(); // Resize input box back to default
        }
    });

    // Function to resize input box based on content
    function resizeInput() {
        userInput.style.height = 'auto';
        userInput.style.height = (userInput.scrollHeight) + 'px';
    }

    // Optional: Adjust the input box size as the user types
    userInput.addEventListener('input', resizeInput);
});
