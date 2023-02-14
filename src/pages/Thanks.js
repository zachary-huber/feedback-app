import { Link } from "react-router-dom";

function Thanks() {
    return (
        <div >
            <img src="http://clipart-library.com/image_gallery2/Thank-You-PNG-Image.png" width="313" length="391"/>
            <p><Link to="/">Create your own server</Link></p>
        </div>
    );
  }
  
  export default Thanks;