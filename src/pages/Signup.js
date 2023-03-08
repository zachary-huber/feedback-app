
function Signup() {
    return (
        <div class="auth">

        <div class="card">
    
          <div class="auth__header text-center">
            <h2>Sign up</h2>
          </div>
          
          <form action="{% url 'signup' %}" method = "POST" class="form auth__form">

            <div class="form__field">
              <input class="input input--text" id="formInput#text" type="text" name="fname"
                placeholder="First name" />
            </div>
    
            <div class="form__field">
                <input class="input input--text" id="formInput#text" type="text" name="lname"
                  placeholder="Last name" />
            </div>
    
            <div class="form__field">
                <input class="input input--text" id="formInput#text" type="text" name="username"
                  placeholder="Email" />
            </div>
    
              <div class="form__field">
                <input class="input input--password" id="formInput#passowrd" type="password" name="password"
                  placeholder="Password" />
              </div>
    
            <div class="auth__actions">
              <input class="btn btn--sub btn--lg" type="submit" value="Sign up" />
            </div>
    
          </form>
          
        </div>
      </div>
    );
  }

export default Signup;