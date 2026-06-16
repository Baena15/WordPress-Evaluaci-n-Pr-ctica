<?php if ( ! defined( 'ABSPATH' ) ) { exit; } ?>

<footer class="site-footer">
    <div class="footer-container">
        <div>
            <h3>UrbanFit Gym</h3>
            <p>Entrena fuerte. Vive mejor.</p>
            <p>📍 Calle Fitness, 123<br>30001 Ciudad deportiva</p>
            <p>📞 <a href="tel:+34900123456">+34 900 123 456</a></p>
        </div>
        <div>
            <h3>Enlaces rápidos</h3>
            <ul style="list-style:none; padding:0;">
                <li><a href="<?php echo home_url('/'); ?>">Inicio</a></li>
                <li><a href="<?php echo home_url('/nosotros/'); ?>">Nosotros</a></li>
                <li><a href="<?php echo home_url('/servicios/'); ?>">Servicios</a></li>
                <li><a href="<?php echo home_url('/blog/'); ?>">Blog</a></li>
                <li><a href="<?php echo home_url('/contacto/'); ?>">Contacto</a></li>
                <li><a href="<?php echo home_url('/politica-de-privacidad/'); ?>">Política de Privacidad</a></li>
            </ul>
        </div>
        <div>
            <h3>Síguenos</h3>
            <p>
                <a href="https://facebook.com/urbanfitgym" target="_blank" rel="noopener">Facebook</a> |
                <a href="https://instagram.com/urbanfitgym" target="_blank" rel="noopener">Instagram</a> |
                <a href="https://twitter.com/urbanfitgym" target="_blank" rel="noopener">Twitter</a>
            </p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>&copy; <?php echo date('Y'); ?> UrbanFit Gym. Todos los derechos reservados.</p>
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
