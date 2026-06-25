ZIP_ADJUSTMENTS = {
    "75028": 500,
    "10001": 1000,
    "90210": 1500
}


def calculate_price(
        base_price: float,
        zip_code: str):

    adjustment = ZIP_ADJUSTMENTS.get(
        zip_code,
        750
    )

    final_price = (
        base_price +
        adjustment
    )

    return {
        "base_price": base_price,
        "adjustment": adjustment,
        "final_price": final_price
    }