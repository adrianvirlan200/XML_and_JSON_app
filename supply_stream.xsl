<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>Supply Stream Orders</title>
                <style>
                    table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                    padding: 5px;
                    text-align: left;
                    }
                </style>
            </head>
            <body>
                <h1>Order Details</h1>
                <xsl:apply-templates select="supply_stream/order" />
            </body>
        </html>
    </xsl:template>

    <xsl:template match="order">
        <h2>Order ID: <xsl:value-of select="@id" /></h2>
        <p>Date: <xsl:value-of select="date/day" />-<xsl:value-of
                select="date/month" />-<xsl:value-of select="date/year" /></p>
        <p>Supplier: <xsl:value-of
                select="supplier_name" /></p>
        <p>Total Price: <xsl:value-of select="order_price" /> <xsl:value-of
                select="order_price/@currency" /></p>

        <table>
            <tr>
                <th>Product Name</th>
                <th>Category</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Total Price</th>
            </tr>
            <xsl:apply-templates select="products/product" />
        </table>
    </xsl:template>

    <xsl:template match="product">
        <tr>
            <td>
                <xsl:value-of select="product_name" />
            </td>
            <td>
                <xsl:value-of select="category" />
            </td>
            <td>
                <xsl:value-of select="quantity" />
            </td>
            <td>
                <xsl:value-of select="unit_price" />
            </td>
            <td>
                <xsl:value-of select="quantity * unit_price" />
            </td>
        </tr>
    </xsl:template>

</xsl:stylesheet>