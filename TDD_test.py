def test_read()
    assert read(inventory.json) == [ { "name": "Mechanical Keyboard", "price": 120.50, "count": 5 }, 
{ "name": "Wireless Mouse", "price": 45.99, "count": 12 }, 
{ "name": "4K Monitor (27 inch)", "price": 349.00, "count": 3 }, 
{ "name": "RGB LED Strip", "price": 19.99, "count": 50 }, 
{ "name": "Ergonomic Chair", "price": 280.75, "count": 1 } ]


def test_str()
    assert inventory.str() == print([['Mechanical Keyboard', 120.50, 5],
    ['Wireless Mouse', 45.99, 12],
     ['4K Monitor (27 inch)', 249.00, 3],
      ['RGB LED Strip', 19.99, 50],
       ['Ergonomic Chair', 280.75, 1]])
