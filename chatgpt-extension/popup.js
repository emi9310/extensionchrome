document.addEventListener('DOMContentLoaded', function() {
    var openChatGPT = document.getElementById('open-chatgpt');
  
    openChatGPT.addEventListener('click', function() {  
      var conversationUrl = 'https://chat.openai.com/';
      chrome.windows.create({
        url: conversationUrl,
        type: 'popup',
        width: 420,
        height: 600,
        left: screen.width - 410,
        top: screen.height - 610
      });
    });
  });
  