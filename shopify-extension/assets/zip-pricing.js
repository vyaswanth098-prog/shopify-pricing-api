document.addEventListener("DOMContentLoaded", () => {

    const button =
        document.getElementById("check-price-btn");

    button.addEventListener("click", async () => {

        const zipCode =
            document.getElementById("zip-code").value;

        const resultDiv =
            document.getElementById("price-result");

        if (!zipCode) {

            resultDiv.innerHTML =
                "Please enter ZIP code";

            return;
        }

        resultDiv.innerHTML =
            "Checking price...";

        try {

            const response =
                await fetch(
                    "https://YOUR-RENDER-URL/pricing",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type":
                                "application/json"
                        },
                        body: JSON.stringify({
                            product_id:
                                window.productId,
                            zip_code:
                                zipCode
                        })
                    }
                );

            const data =
                await response.json();

            resultDiv.innerHTML = `
                <div class="price-card">
                    <div class="price-label">
                        Location Specific Price
                    </div>

                    <div class="price-value">
                        $${data.price}
                    </div>

                    <div class="availability">
                        ✓ Available For Delivery
                    </div>
                </div>
            `;

        } catch (error) {

            resultDiv.innerHTML =
                "Unable to fetch pricing";
        }
    });
});