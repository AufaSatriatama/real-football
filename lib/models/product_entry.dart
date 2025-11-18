// To parse this JSON data, do
//
//     final productEntry = productEntryFromJson(jsonString);

import 'dart:convert';

List<ProductEntry> productEntryFromJson(String str) => List<ProductEntry>.from(json.decode(str).map((x) => ProductEntry.fromJson(x)));

String productEntryToJson(List<ProductEntry> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class ProductEntry {
    String id;
    String name;
    String title;
    String description;
    int price;
    String category;
    String thumbnail;
    DateTime createdAt;
    bool isFeatured;
    dynamic userId;
    dynamic userUsername;

    ProductEntry({
        required this.id,
        required this.name,
        required this.title,
        required this.description,
        required this.price,
        required this.category,
        required this.thumbnail,
        required this.createdAt,
        required this.isFeatured,
        required this.userId,
        required this.userUsername,
    });

    factory ProductEntry.fromJson(Map<String, dynamic> json) => ProductEntry(
        id: json["id"],
        name: json["name"],
        title: json["title"],
        description: json["description"],
        price: json["price"],
        category: json["category"],
        thumbnail: json["thumbnail"],
        createdAt: DateTime.parse(json["created_at"]),
        isFeatured: json["is_featured"],
        userId: json["user_id"],
        userUsername: json["user_username"],
    );

    Map<String, dynamic> toJson() => {
        "id": id,
        "name": name,
        "title": title,
        "description": description,
        "price": price,
        "category": category,
        "thumbnail": thumbnail,
        "created_at": createdAt.toIso8601String(),
        "is_featured": isFeatured,
        "user_id": userId,
        "user_username": userUsername,
    };
}
