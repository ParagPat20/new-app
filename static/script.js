// Function to fetch ingredients from db.json
async function fetchIngredients() {
  try {
    const response = await fetch("db.json"); // Ensure this path is correct
    const data = await response.json(); // Parse JSON data

    const container = document.getElementById("ingredients-container");

    // Loop through each ingredient and create divs
    data[0].data.forEach((ingredient) => {
      // Create the ingredient div
      const ingDiv = document.createElement("div");
      ingDiv.classList.add("ing-item");

      // Create the label for the checkbox
      const label = document.createElement("label");
      label.classList.add("btn-checkbox");

      // Create the checkbox input
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.classList.add("checkbox");

      // Add event listener to the checkbox
      checkbox.addEventListener("change", () => {
        const checkedCheckboxes =
          document.querySelectorAll(".checkbox:checked");
        if (checkedCheckboxes.length > 10) {
          checkbox.checked = false; // Prevent selection beyond 10
          alert("You can only select up to 10 ingredients."); // Optional: Alert the user
        } else {
          updateSelectedCount();
        }
      });

      // Create the image element
      const img = document.createElement("img");
      img.src = "img/ing2.gif"; // Change to dynamic source if needed
      img.alt = `Ingredient - ${ingredient.ING_Name}`;

      // Create the paragraph for ingredient name
      const para = document.createElement("p");
      para.textContent = ingredient.ING_Name;

      // Append elements to label, then to ingDiv
      label.appendChild(checkbox);
      label.appendChild(img);
      label.appendChild(para);
      ingDiv.appendChild(label);

      // Append ingDiv to the container
      container.appendChild(ingDiv);
    });
  } catch (error) {
    console.error("Error fetching ingredients:", error);
  }
}

// Call the function to fetch ingredients when the page loads
fetchIngredients();

// Function to update the selected ingredients count
function updateSelectedCount() {
  const checkboxes = document.querySelectorAll(".checkbox");
  const selectedCountElement = document.querySelector(".fi-top p span");
  let selectedCount = 0;

  checkboxes.forEach((checkbox) => {
    if (checkbox.checked) {
      selectedCount++;
    }
  });

  // Update the count display
  selectedCountElement.textContent = `${selectedCount}/10`;
}

// Add event listeners to checkboxes
checkbox.addEventListener("change", () => {
  const checkedCheckboxes = document.querySelectorAll(".checkbox:checked");
  if (checkedCheckboxes.length > 10) {
    checkbox.checked = false; // Prevent selection beyond 10
    alert("You can only select up to 10 ingredients."); // Optional: Alert the user
  } else {
    updateSelectedCount();
  }
});
