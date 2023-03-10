import { Link } from "react-router-dom";

function Login() {
    return (
        <div class="auth">

    <div class="card">

      <div class="auth__header text-center">
        <h2>Account Login</h2>
      </div>


      <form  method = "POST" class="form auth__form">

        <div class="form__field">
          <input class="input input--text" id="formInput#text" type="text" name="username"
            placeholder="Email" />
        </div>

        <div class="form__field">
          <input class="input input--password" id="formInput#passowrd" type="password" name="password"
            placeholder="Password" />
        </div>
        <div class="auth__actions">
          <input class="btn btn--sub btn--lg" type="submit" value="Login" />
        </div>
        <div class="auth__alternative">
          <p>Don’t have an Account?</p>
          <a href="">Sign Up</a>
        </div>

      </form>
    </div>
  </div>

    );
  }
  
  export default Login;