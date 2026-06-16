<?php
add_action( 'wp_enqueue_scripts', function() {
    wp_enqueue_style( 'urbanfit-parent-style', get_template_directory_uri() . '/style.css' );
    wp_enqueue_style( 'urbanfit-child-style', get_stylesheet_uri(), array('urbanfit-parent-style') );
} );
