document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.querySelector('.chat-body');
    const userInput = document.getElementById('user-input');
    const sendButton = document.querySelector('.send-btn');

     // JS functionality to handle sending messages
     document.getElementById('send-btn').addEventListener('click', function () {
        let userInput = document.getElementById('user-input').value;
        if (userInput.trim() !== '') {
            let chatBody = document.getElementById('chat-body');
            let userMessage = `<div class="user-message">${userInput}</div>`;
            chatBody.innerHTML += userMessage;
            document.getElementById('user-input').value = '';
            
            // Simulate bot response with loading indicator
            chatBody.innerHTML += `<div class="loading-dots"><span></span><span></span><span></span></div>`;
            
            setTimeout(() => {
                document.querySelector('.loading-dots').remove();
                chatBody.innerHTML += `<div class="bot-message">I'm processing your request...</div>`;
                chatBody.scrollTop = chatBody.scrollHeight;
            }, 2000);
            
            chatBody.scrollTop = chatBody.scrollHeight; // Auto scroll to bottom
        }
    });

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
