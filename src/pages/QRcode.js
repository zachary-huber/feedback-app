
function QRcode() {
    return (
        <div>
    <h2>Survey Name:</h2>

    <div>
        <img id='barcode' src="https://api.qrserver.com/v1/create-qr-code/?data=HelloWorld&amp;size=150x150" alt="" width="150" height="150" />
    </div>
    
    <a href="{% url 'landingpage' %}">Back to landing</a>

  </div>
    );
  }
  
  export default QRcode;