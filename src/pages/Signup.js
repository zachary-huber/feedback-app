import { Link } from "react-router-dom";
import Button from '@mui/material/Button';

function Signup() {
    return (
        <div>
        <h1>this is the where the signup page will go</h1>
        <Link to="/">
            <Button variant="outlined">
                Sign up
            </Button>
        </Link>
        </div>
    );
  }
  
  export default Signup;