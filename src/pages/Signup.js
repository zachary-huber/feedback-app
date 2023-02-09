
function Signup() {
    return (
        <div class="card">
            <div class="callToAction">
                <h2>Sign up</h2>
                    <form action="">
                        <input type="text" id="fname" name="fname" placeholder="First name"/><br/>
                        <input type="text" id="lname" name="lname" placeholder="Last name"/><br/>
                        <input type="email" id="email" name="email" placeholder="Email"/><br/>
                        <input type="password" id="pass" name="pass" placeholder="Password"/><br/>

                        <input type="checkbox" id="consent" name="consent" value="consent"/>
                        <label for="consent">I consent to the privacy policy</label><br/><br/>

                        <input type="submit" value="Sign up"/>  
                    </form>
            </div>
        </div>
    );
  }
  
  export default Signup;