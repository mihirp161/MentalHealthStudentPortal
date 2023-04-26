// // Get the form and button elements
// const form = document.querySelector('#registration-form');
// const registerButton = document.querySelector('#register-button');
// const backButton = document.querySelector('#back-button');
// const successMessage = document.querySelector('#success-message');

// // Add event listener for form submission
// form.addEventListener('submit', (event) => {
//   // Prevent form from submitting
//   event.preventDefault();
  
//   // Get form values
//   const name = document.querySelector('#name').value;
//   const address = document.querySelector('#address').value;
//   const phone = document.querySelector('#phone').value;
//   const school = document.querySelector('#school').value;
//   const year = document.querySelector('#year').value;
//   const dob = document.querySelector('#dob').value;
  
//   // Validate form values (for example, check that required fields are not empty)
//   if (!name || !address || !phone || !school || !year || !dob) {
//     alert('Please fill in all required fields.');
//     return;
//   }

//   const formData = new FormData(event.target);
//   // log the data being submitted
//   for (const [key, value] of formData.entries()) {
//     console.log(`${key}: ${value}`);
//   }
  
//   // Perform AJAX request to submit form data to server (replace with your own code)
//   // You can use the Fetch API or jQuery AJAX to do this
//   fetch('/register', {
//     method: 'POST',
//     body: JSON.stringify({
//       name,
//       address,
//       phone,
//       school,
//       year,
//       dob
//     }),
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   })
//   .then(response => {
//     if (response.ok) {
//       // Show success message
//       successMessage.textContent = 'Registration successful!';
//       successMessage.style.color = 'green';
      
//       // Hide register button and show back button
//       registerButton.style.display = 'none';
//       backButton.style.display = 'inline-block';
      
//       // Add a new function to update the page with the success message
//       updatePageWithSuccessMessage();
//     } else {
//       // Show error message
//       alert('An error occurred while submitting the form. Please try again later.');
//     }
//   })
//   .catch(error => {
//     console.error(error);
//     alert('An error occurred while submitting the form. Please try again later.');
//   });
// });

// // Add event listener for back button click
// backButton.addEventListener('click', (event) => {
//   // Prevent button from submitting form
//   event.preventDefault();
  
//   // Reset form values (optional)
//   form.reset();
  
//   // Hide success message and back button and show register button
//   successMessage.textContent = '';
//   successMessage.style.color = 'inherit';
//   backButton.style.display = 'none';
//   registerButton.style.display = 'inline-block';
// });

// // Add a new function to update the page with the success message
// function updatePageWithSuccessMessage() {
//   // Replace the form with the success message
//   form.style.display = 'none';
//   successMessage.style.display = 'block';
  
//   // Optionally, add a button to return to the form
//   const returnButton = document.createElement('button');
//   returnButton.textContent = 'Return to form';
//   successMessage.appendChild(returnButton);
  
//   // Add event listener to the return button
//   returnButton.addEventListener('click', (event) => {
//     event.preventDefault();
    
//     // Hide success message and show form
//     form.style.display = 'block';
//     successMessage.style.display = 'none';
//   });
// }
