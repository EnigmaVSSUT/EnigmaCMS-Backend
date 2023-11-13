import db from "../../db/client.js"

export const saveToDatabase = (blog) => {
    // Save to database
        return db.Blog.create({
            data:blog
        });

}

// export const getAllBlogs = async () => {
//     try {
//         const blogs = await db.Blog.findAll();
//         return blogs;
//     } catch (error) {
//         console.log(error);
//         return [];
//     }
// }