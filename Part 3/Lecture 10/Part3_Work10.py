'დავალების ქომანდები რიგის მიხედვით:'

CREATE TABLE Mobiles (
    number INTEGER
    brand VARCHAR
    model VARCHAR
    price FLOAT
    quantity INTEGER
    color VARCHAR
    length FLOAT
    width FLOAT
);

'მოცემული ქომანდით შევქმენი Mobiles თეიბლი, რომელსაც გადაეცა შესაბამისი სვეტები და მათი ტიპები'
'ახლა საჭიროა, ამ სვეტებში ჩავწეროთ ინფორმაცია რიგითობისა და ტიპების დაცვით:'

INSERT INTO Mobiles VALUES
    (1, "Iphone", "X", 800, 10, "Black", 16.9, 6.4),
    (2, "Samsung", "galaxy s20", 850, 3, "Blue", 18.2, 6.2),
    (3, "Iphone", "15 Pro", 1200, 1, "Blue", 18.3, 6.5)
    (4, "Xiaomi", "Redmi note 10s", 500, 5, "Blue", 17.4, 6.2);


'გამოვიტანოთ ყველა მობილური, რომელიც 600-ზე მეტი ღირს'

SELECT * FROM Mobiles WHERE price > 600;
"ასეთი იქნება ყველა, მე-4-ს გარდა"


'გამოვიტანოთ ყველა მობილური, რომელიც 2 ცალზე მეტი გვაქვს და ლურჯია'

SELECT * FROM Mobiles WHERE quantity > 2 AND Color = "Blue";
"ასეთი იქნება 2 და 4"


'თანხას ვამრავლებ რაოდენობაზე ყველა პროდუქტისთვის:'

SELECT *, price * quantity AS total_value FROM Mobiles;


'გამომაქვს ყველა პროდუქტი, რომელთა ფართობი მეტია 10-ზე'

SELECT *, length * width AS area FROM Mobiles WHERE area > 10;
"გამოიტანს ყველა პროდუქტს"