// /* eslint-disable no-undef */
// /* eslint-disable no-unused-vars */
// import React, { useState } from 'react';
// import imageSrc from '../images/Allura - Feedback Session.png';
// import { Link } from 'react-router-dom';
// import "../CSS/login.css"

// function LoginPage() {
//     const [name, setName] = useState('');
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [confirmPassword, setConfirmPassword] = useState('');
//     const [rememberMe, setRememberMe] = useState(false);

//     const handleNameChange = (e) => {
//         setName(e.target.value);
//     };

//     const handleEmailChange = (e) => {
//         setEmail(e.target.value);
//     };

//     const handlePasswordChange = (e) => {
//         setPassword(e.target.value);
//     };

//     const handleConfirmPasswordChange = (e) => {
//         setConfirmPassword(e.target.value);
//     };

//     const handleRememberMeChange = (e) => {
//         setRememberMe(e.target.checked);
//     };


//     const handleSubmit = (e) => {
//         e.preventDefault();

//         // Form validation checks
//         if (!name || !email || !password || !confirmPassword) {
//             // Display popup message or error notification
//             alert('Please fill in all fields');
//             return;
//         }

//         if (password !== confirmPassword) {
//             // Display popup message or error notification
//             alert('Passwords do not match');
//             return;
//         }

//         // If all validation checks pass, proceed with form submission logic
//         // Handle login functionality, API requests, etc.
//         // You can access the form values using the state variables (name, email, password, confirmPassword)
//     };

//     return (
//         <div className='big-container'>
//         <div className='container'>
           
//             <form className='login-form' onSubmit={handleSubmit}>
//                     <h2>Login</h2>
//                 <div>
//                     <label htmlFor="name">Name</label>
//                     <input type="text" id="name" value={name} onChange={handleNameChange} />
//                 </div>
//                 <div>
//                     <label htmlFor="email">Email</label>
//                     <input type="email" id="email" value={email} onChange={handleEmailChange} />
//                 </div>
//                 <div>
//                     <label htmlFor="password">Password</label>
//                     <input type="password" id="password" value={password} onChange={handlePasswordChange} />
//                 </div>
//                 <div>
//                     <label htmlFor="confirmPassword">Confirm Password</label>
//                     <input
//                         type="password"
//                         id="confirmPassword"
//                         value={confirmPassword}
//                         onChange={handleConfirmPasswordChange}
//                     />
//                 </div>
//                     <div className="additional-options">
//                         <div className="remember-me">
//                             <input
//                                 type="checkbox"
//                                 id="rememberMe"
//                                 checked={rememberMe}
//                                 onChange={handleRememberMeChange}
//                             />
//                             <label htmlFor="rememberMe">Remember Me</label>
//                         </div>
//                         <div className="forgot-password">
//                             <Link to="/forgot-password">Forgot Password</Link>
//                         </div>
//                     </div>
//                 <button type="submit">Login</button>
//                     <p className="signup-link">
//                         Dont have an account? <Link to="/signup">Sign Up</Link>
//                     </p>
//             </form>
//         </div>
//         <div className='img-container'>
//                 <img className='img-blush' src={imageSrc} alt="Image" />
//         </div>
//         </div>
//     );
// }

// export default LoginPage;

