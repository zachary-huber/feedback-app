import { Link } from "react-router-dom";

function Login() {
    return (
        <div class="card">
            <div class="callToAction">
                <h2>Log in</h2>
                    <form action="">
                        <input type="email" id="email" name="email" placeholder="Email"/><br/>
                        <input type="password" id="pass" name="pass" placeholder="Password"/><br/>
                        <input type="submit" value="Log in"/>
                    </form>
                    <p>No account? <Link to="/signup">sign up.</Link></p>
            </div>
        </div>
    );
  }
  
  export default Login;