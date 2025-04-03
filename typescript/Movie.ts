/**
 * Interface representing a Movie in the database
 */
export interface Movie {
    /**
     * The title of the movie (primary key)
     */
    title: string;
    
    /**
     * The release year of the movie (sort key)
     */
    year: number;
    
    /**
     * A brief summary of the movie's plot
     */
    plot?: string;
    
    /**
     * The movie's rating on a scale of 1-10
     */
    rating?: number;
    
    /**
     * Optional list of actors in the movie
     */
    actors?: string[];
    
    /**
     * Optional director of the movie
     */
    director?: string;
}
