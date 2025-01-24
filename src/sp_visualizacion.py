import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def visualizar_col_categoricas(df, max_categories=20):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) == 0:
        print("No hay columnas categóricas")
        return
    
    # Configurar el tamaño de la figura
    num_cols = len(categorical_cols)
    rows = (num_cols + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten()  # Asegurarse de que `axes` sea un arreglo unidimensional
    
    # Generar gráficos para columnas categóricas
    for i, col in enumerate(categorical_cols):
        value_counts = df[col].value_counts()
        if len(value_counts) > max_categories:
            top_categories = value_counts.head(max_categories).index
            filtered_df = df[df[col].isin(top_categories)]
        else:
            filtered_df = df
        
        sns.countplot(data=filtered_df, x=col, ax=axes[i], order=value_counts.index[:max_categories])
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90)
    
    # Eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(len(categorical_cols), len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()

    
    # Ajustar diseño
    plt.tight_layout()
    plt.show()