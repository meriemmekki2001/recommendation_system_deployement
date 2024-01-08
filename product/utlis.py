from .models import AprioriResults, Product

def get_association_rules_recommendations(product_id):
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return []

    
    association_results = AprioriResults.objects.filter(
        antecedents__isnull=False,
        consequents__isnull=False
    )

    
    recommended_products_set = set()


    for result in association_results:
        antecedents = result.antecedents.split(", ")  

        
        if product.title in antecedents:
            consequents = result.consequents.split(", ")  

        
            recommended_products_set.update(
                Product.objects.filter(title__in=consequents)
            )


    recommended_products = list(recommended_products_set)
    
    return recommended_products


