<?php
add_action( 'wp_enqueue_scripts', function() {
    wp_enqueue_style( 'urbanfit-parent-style', get_template_directory_uri() . '/style.css' );
    wp_enqueue_style( 'urbanfit-child-style', get_stylesheet_uri(), array('urbanfit-parent-style') );
} );

/**
 * Shortcode: listado profesional de posts recientes para la página Blog.
 * Uso: [urbanfit_recent_posts]
 */
add_shortcode( 'urbanfit_recent_posts', function( $atts ) {
    $args = shortcode_atts( array(
        'posts' => 6,
    ), $atts, 'urbanfit_recent_posts' );

    $query = new WP_Query( array(
        'post_type'      => 'post',
        'posts_per_page' => intval( $args['posts'] ),
        'post_status'    => 'publish',
    ) );

    if ( ! $query->have_posts() ) {
        return '<p style="text-align:center; color:#6b7280;">Próximamente publicaremos contenido en el blog.</p>';
    }

    ob_start();
    ?>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        <?php while ( $query->have_posts() ) : $query->the_post(); ?>
            <article style="background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.05); display: flex; flex-direction: column;">
                <?php if ( has_post_thumbnail() ) : ?>
                    <a href="<?php the_permalink(); ?>" style="display: block;">
                        <?php the_post_thumbnail( 'medium_large', array( 'style' => 'width: 100%; height: 220px; object-fit: cover; display: block;' ) ); ?>
                    </a>
                <?php endif; ?>
                <div style="padding: 28px; flex: 1; display: flex; flex-direction: column;">
                    <p style="font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #ff6b35; margin-bottom: 8px;"><?php echo get_the_date(); ?></p>
                    <h3 style="font-family: 'Oswald', sans-serif; font-size: 1.35rem; font-weight: 700; text-transform: uppercase; margin-bottom: 12px; line-height: 1.2;">
                        <a href="<?php the_permalink(); ?>" style="color: #18181b;"><?php the_title(); ?></a>
                    </h3>
                    <p style="color: #4b5563; line-height: 1.6; margin-bottom: 20px; flex: 1;"><?php echo wp_trim_words( get_the_excerpt(), 18 ); ?></p>
                    <a href="<?php the_permalink(); ?>" style="color: #ff6b35; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em;">Leer más →</a>
                </div>
            </article>
        <?php endwhile; ?>
    </div>
    <?php
    wp_reset_postdata();
    return ob_get_clean();
} );
