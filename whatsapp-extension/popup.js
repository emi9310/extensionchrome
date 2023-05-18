document.addEventListener('DOMContentLoaded', function() {
    var openWhatsAppButton = document.getElementById('open-whatsapp');
  
    openWhatsAppButton.addEventListener('click', function() {  
      var conversationUrl = 'https://web.whatsapp.com/';
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
  