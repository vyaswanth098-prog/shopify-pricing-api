ZIP_ADJUSTMENTS = {
    "75028": 200,
    "10001": 400,
    "90210": 500
}


def calculate_price(
        base_price: float,
        zip_code: str):

    adjustment = ZIP_ADJUSTMENTS.get(
        zip_code,
        300
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