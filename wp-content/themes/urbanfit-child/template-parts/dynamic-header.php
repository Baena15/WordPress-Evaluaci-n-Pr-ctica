<?php
/**
 * Header personalizado de UrbanFit Gym.
 *
 * Sobreescribe la plantilla dinámica de Hello Elementor.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$site_name = get_bloginfo( 'name' );
$tagline   = get_bloginfo( 'description', 'display' );
$home_url  = esc_url( home_url( '/' ) );
$contact_url = esc_url( home_url( '/contacto/' ) );

$menu_args = [
	'theme_location' => 'menu-1',
	'fallback_cb'    => false,
	'container'      => false,
	'menu_class'     => 'uf-menu',
	'echo'           => false,
];

$nav_menu = wp_nav_menu( $menu_args );
?>
<header class="uf-header" id="uf-header">
	<div class="uf-header-inner">
		<a href="<?php echo $home_url; ?>" class="uf-branding" aria-label="<?php echo esc_attr( $site_name ); ?>">
			<span class="uf-branding-text">
				<span class="uf-site-title">
					<span class="uf-brand-white">UrbanFit</span><span class="uf-brand-accent">Gym</span>
				</span>
				<?php if ( $tagline ) : ?>
					<span class="uf-site-tagline"><?php echo esc_html( $tagline ); ?></span>
				<?php endif; ?>
			</span>
		</a>

		<?php if ( $nav_menu ) : ?>
			<nav class="uf-nav" aria-label="<?php esc_attr_e( 'Main menu', 'urbanfit-child' ); ?>">
				<?php echo $nav_menu; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
			</nav>
		<?php endif; ?>

		<a href="<?php echo $contact_url; ?>" class="uf-header-cta">Únete</a>

		<button type="button" class="uf-nav-toggle" aria-label="<?php esc_attr_e( 'Toggle menu', 'urbanfit-child' ); ?>" aria-expanded="false" aria-controls="uf-mobile-nav">
			<span></span>
			<span></span>
			<span></span>
		</button>
	</div>

	<?php if ( $nav_menu ) : ?>
		<nav class="uf-mobile-nav" id="uf-mobile-nav" aria-label="<?php esc_attr_e( 'Mobile menu', 'urbanfit-child' ); ?>" aria-hidden="true" inert>
			<?php
			$mobile_menu_args          = $menu_args;
			$mobile_menu_args['menu_class'] = 'uf-mobile-menu';
			wp_nav_menu( $mobile_menu_args );
			?>
			<a href="<?php echo $contact_url; ?>" class="uf-header-cta">Únete</a>
		</nav>
	<?php endif; ?>
</header>

<script>
(function() {
	const toggle = document.querySelector('.uf-nav-toggle');
	const mobileNav = document.getElementById('uf-mobile-nav');
	if (!toggle || !mobileNav) return;

	toggle.addEventListener('click', function() {
		const isOpen = mobileNav.classList.toggle('is-open');
		toggle.classList.toggle('is-active', isOpen);
		toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
		mobileNav.setAttribute('aria-hidden', isOpen ? 'false' : 'true');
		if (isOpen) {
			mobileNav.removeAttribute('inert');
		} else {
			mobileNav.setAttribute('inert', '');
		}
	});

	// Cerrar menú al hacer click en un enlace (navegación fluida en la misma página)
	mobileNav.querySelectorAll('a').forEach(function(link) {
		link.addEventListener('click', function() {
			mobileNav.classList.remove('is-open');
			toggle.classList.remove('is-active');
			toggle.setAttribute('aria-expanded', 'false');
			mobileNav.setAttribute('aria-hidden', 'true');
			mobileNav.setAttribute('inert', '');
		});
	});
})();
</script>
