
function LandingPage() {
    return (
        <div>
        <h2>Hello fname!</h2>
    
        <a href="{% url 'landingpage' %}">+ Create New Survey</a>
            <div>
                <div class="dropdown">
                    survey name
                    <b class="dropbtn"> &#x22EE;</b>
                    <div class="dropdown-content">
                      <a href="#">Delete</a>
                      <a href="#">Get QR</a>
                    </div>
                  </div>
            </div>
      </div>
    );
  }
  
  export default LandingPage;