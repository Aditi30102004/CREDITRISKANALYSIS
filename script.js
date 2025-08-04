document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("loanForm").addEventListener("submit", async function (event) {
        event.preventDefault();

        // ✅ Collect form data
        let data = {
            status_checking: parseInt(document.getElementById("status_checking").value),
            duration: parseInt(document.getElementById("duration").value),
            credit_history: 2,  // Default value, update as needed
            purpose: 1,  // Default value, update as needed
            credit_amount: parseInt(document.getElementById("credit_amount").value),
            savings_account: 1, // Default value, update as needed
            employment_since: 12, // Default value, update as needed
            installment_rate: 2, // Default value, update as needed
            personal_status: 1, // Default value, update as needed
            other_debtors: 0, // Default value, update as needed
            residence_since: 2, // Default value, update as needed
            property: 1, // Default value, update as needed
            age: parseInt(document.getElementById("age").value),
            other_installment_plans: 0, // Default value, update as needed
            housing: 1, // Default value, update as needed
            existing_credits: 2, // Default value, update as needed
            job: 2, // Default value, update as needed
            liable_people: 1, // Default value, update as needed
            telephone: 1, // Default value, update as needed
            foreign_worker: 1 // Default value, update as needed
        };

        console.log("📤 Sending Data:", data);

        try {
            let response = await fetch("http://127.0.0.1:8000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            let result = await response.json();
            console.log("✅ Response Received:", result);

            // ✅ Display Result
            document.getElementById("result").innerText = result.credit_risk || "Error in prediction!";
        } catch (error) {
            console.error("❌ Error:", error);
            document.getElementById("result").innerText = "Server error, please try again!";
        }
    });
});
