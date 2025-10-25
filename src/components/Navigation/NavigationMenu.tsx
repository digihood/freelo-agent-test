import React, { useState, useEffect, useRef } from 'react';
import { useMediaQuery } from '../../hooks/useMediaQuery';
import { HamburgerIcon } from './HamburgerIcon';
import { NavigationItem, NavigationItemProps } from './NavigationItem';

export interface NavigationMenuProps {
  items: Omit<NavigationItemProps, 'onClick'>[];
  logo?: React.ReactNode;
  onItemClick?: (href: string) => void;
}

/**
 * Main responsive navigation component
 * Renders horizontal menu on desktop and collapsible menu on mobile
 * Manages menu toggle state and handles outside clicks to close menu
 */
export const NavigationMenu: React.FC<NavigationMenuProps> = ({
  items,
  logo,
  onItemClick,
}) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const screenSize = useMediaQuery();
  const menuRef = useRef<HTMLDivElement>(null);
  const isMobile = screenSize === 'mobile';

  // Close menu when screen size changes to desktop
  useEffect(() => {
    if (!isMobile && isMenuOpen) {
      setIsMenuOpen(false);
    }
  }, [isMobile, isMenuOpen]);

  // Handle clicks outside menu to close it
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        isMenuOpen &&
        menuRef.current &&
        !menuRef.current.contains(event.target as Node)
      ) {
        setIsMenuOpen(false);
      }
    };

    if (isMenuOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isMenuOpen]);

  // Handle escape key to close menu
  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape' && isMenuOpen) {
        setIsMenuOpen(false);
      }
    };

    if (isMenuOpen) {
      document.addEventListener('keydown', handleEscape);
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
    };
  }, [isMenuOpen]);

  const toggleMenu = () => {
    setIsMenuOpen((prev) => !prev);
  };

  const handleItemClick = (href: string) => {
    if (isMobile) {
      setIsMenuOpen(false);
    }
    onItemClick?.(href);
  };

  return (
    <nav className="navigation-menu" ref={menuRef} role="navigation">
      <div className="navigation-container">
        {logo && <div className="navigation-logo">{logo}</div>}

        {isMobile && (
          <HamburgerIcon
            isOpen={isMenuOpen}
            onClick={toggleMenu}
          />
        )}

        <div
          className={`navigation-items ${isMobile ? 'mobile' : 'desktop'} ${
            isMenuOpen ? 'open' : ''
          }`}
          role="menu"
        >
          {items.map((item, index) => (
            <NavigationItem
              key={`${item.href}-${index}`}
              {...item}
              onClick={() => handleItemClick(item.href)}
            />
          ))}
        </div>
      </div>

      {/* Overlay for mobile when menu is open */}
      {isMobile && isMenuOpen && (
        <div
          className="navigation-overlay"
          onClick={() => setIsMenuOpen(false)}
          aria-hidden="true"
        />
      )}
    </nav>
  );
};
